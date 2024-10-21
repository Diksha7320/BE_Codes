class Weights:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.pw_ratio = profit / weight

def print_weights(arr):
    print("-----------")
    print(" W  P  P/W")
    for w in arr:
        print(f"{w.weight} {w.profit} {w.pw_ratio:.2f}")
    print("-----------")

def cmp(item):
    return item.pw_ratio

def f_knapsack(arr, capacity):
    arr.sort(key=cmp, reverse=True)
    remaining_capacity = capacity
    total_profit = 0

    for w in arr:
        print(f"Selected -> Weight: {w.weight}, Profit: {w.profit}, P/W Ratio: {w.pw_ratio:.2f}")
        if w.weight <= remaining_capacity:
            remaining_capacity -= w.weight
            total_profit += w.profit
        else:
            total_profit += w.pw_ratio * remaining_capacity
            remaining_capacity = 0
            break
        print(f"Capacity Remaining: {remaining_capacity}, Profit: {total_profit}")
    
    return total_profit

def main():
    n = int(input("Enter Number of Weights: "))
    arr = []

    for i in range(n):
        weight = int(input(f"Enter Weight {i+1}: "))
        profit = int(input(f"Enter Profit {i+1}: "))
        arr.append(Weights(weight, profit))

    print()
    print_weights(arr)

    capacity = int(input("Enter Capacity: "))
    print()
    
    max_profit = f_knapsack(arr, capacity)
    print(f"Maximum Profit: {max_profit}")

if __name__ == "__main__":
    main()
