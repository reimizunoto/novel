from src import xs33

if __name__ == '__main__':
    novel_name = input("Enter the name of the novel: ")
    novel = xs33.Xs33(novel_name)
    novel.download()