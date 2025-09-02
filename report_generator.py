def generate_report():
    try:
        with open("sample_report.txt", "r") as f:
            data = f.read()
        print("\n===== Pen Test Report =====")
        print(data)
        print("===========================\n")
    except FileNotFoundError:
        print("No report found. Run the tools first.")

if __name__ == "__main__":
    generate_report()

