import functions as f


def main():
    f.get_requirements()
    f.data_analysis_1()


# tests whether script being run directly, or being imported by something else
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()
