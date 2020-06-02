class InsertionSort:
    setToSort = [1,2,3,4,5]

    def getSetToSort(self):
        
        print("\tEnter all integers to sort. Enter \'e\' when done: ")
        self.setToSort.clear()
        i = 0
        num = null
        while (num != e):
            i = i+1
            try:
                num = input("\tEnter Num "+i+", or e to end:")
                num = int(num)
                self.setToSort.append(num)
            except Exception:
                print("\tInvalid input. Sorting program will terminate. ")
                break

    def doInsertionSort(self):
        size = len(self.setToSort)
        temp = null
        sortedSet = null

        for i in range(size):
            a = setToSort.pop(0);
            b = setToSort.pop(0);

            if (a>b)








