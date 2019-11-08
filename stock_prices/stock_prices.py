#!/usr/bin/python
import argparse


def find_max_profit(prices):
    stack = []
    max_ = 0
    for i in range(len(prices)):
        print(i, stack)
        if not stack:
            stack.append(i)
        elif prices[i] >= prices[stack[-1]]:
            stack.append(i)
        else:
            new_max = prices[stack[-1]] - prices[stack[0]]
            if new_max > max_:
                max_ = new_max
            stack.clear()
            stack.append(i)
    if stack:
        new_max = prices[stack[-1]] - prices[stack[0]]
        if new_max > max_:
            max_ = new_max
    # If we haven't found any increasing runs, the price is strictly decreasing
    # and we can safely minimize loss by buying on the second-to-last day and
    # selling on the last.
    if not max_:
        return prices[-1] - prices[-2]
    return max_



if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))