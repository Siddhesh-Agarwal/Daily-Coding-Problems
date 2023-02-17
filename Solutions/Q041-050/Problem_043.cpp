// Implement a stack that has the following methods:

// push(val), which pushes an element onto the stack
// pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
// max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

#include <iostream>
using namespace std;

class Stack
{
private:
    int *arr;
    int top;
    int capacity;
    int max;

public:
    Stack(int size)
    {
        arr = new int[size];
        capacity = size;
        top = -1;
        max = 0;
    }

    bool isFull()
    {
        return top == capacity - 1;
    }

    bool isEmpty()
    {
        return top == -1;
    }

    void push(int x)
    {
        if (isFull())
        {
            cout << "OverFlow";
            return;
        }
        if (x > max)
        {
            max = x;
        }
        arr[++top] = x;
    }

    void pop()
    {
        if (isEmpty())
        {
            cout << "UnderFlow";
            return;
        }
        if (arr[top] == max)
        {
            max = 0;
            for (int i = 0; i < top; i++)
            {
                if (arr[i] > max)
                {
                    max = arr[i];
                }
            }
        }
        top--;
    }

    int max()
    {
        return max;
    }
}
