// Given the root to a binary search tree, find the second largest node in the tree.

#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *left, *right;
};

Node *newNode(int data)
{
    Node *temp = new Node;
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}

Node *insert(Node *node, int data)
{
    if (node == NULL)
        return newNode(data);
    if (data < node->data)
        node->left = insert(node->left, data);
    else if (data > node->data)
        node->right = insert(node->right, data);
    return node;
}

void secondLargestUtil(Node *root, int &c)
{
    if (root == NULL || c >= 2)
        return;
    secondLargestUtil(root->right, c);
    c++;
    if (c == 2)
    {
        cout << "2nd largest element is " << root->data << endl;
        return;
    }
    secondLargestUtil(root->left, c);
}

void secondLargest(Node *root)
{
    int c = 0;
    secondLargestUtil(root, c);
}

int main()
{
    Node *root = NULL;
    root = insert(root, 20);
    insert(root, 8);
    insert(root, 22);
    insert(root, 4);
    insert(root, 12);
    insert(root, 10);
    insert(root, 14);
    secondLargest(root);
    return 0;
}