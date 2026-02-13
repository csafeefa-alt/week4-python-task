def read_file(fname):
    try:
        f = open(fname, "r")
        lines = f.readlines()
        f.close()

        if len(lines) == 0:
            raise ValueError("File is empty.")

        total = 0
        valid = 0
        invalid = 0

        print("\nStudent Marks\n")

        for i, line in enumerate(lines, start=1):
            line = line.strip()

            if line == "":
                invalid += 1
                print("Line", i, ": Invalid (empty line)")
                continue

            try:
                parts = line.split(",")

                if len(parts) != 2:
                    raise ValueError("Incorrect format")

                name = parts[0].strip()
                mark_text = parts[1].strip()

                if name == "":
                    raise ValueError("Name missing")

                marks = int(mark_text)

                if marks < 0 or marks > 100:
                    raise ValueError("Marks out of range")

                print(name, "-", marks)
                total += marks
                valid += 1

            except ValueError:
                invalid += 1
                print("Line", i, ": Invalid record ->", line)

        if valid == 0:
            print("\nNo valid records found. Average cannot be calculated.")
        else:
            avg = total / valid
            print("\nAverage marks:", round(avg, 2))

        print("\nValid records:", valid)
        print("Invalid records:", invalid)

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as e:
        print("Error:", e)


fname = input("Enter file name: ")
read_file(fname)