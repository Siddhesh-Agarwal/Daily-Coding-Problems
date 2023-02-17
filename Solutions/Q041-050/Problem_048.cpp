// This problem was asked by Google.

// Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

// For example, given the following preorder traversal:

// [a, b, d, e, c, f, g]

// And the following inorder traversal:

// [d, b, e, a, f, c, g]

// You should return the following tree:

//     a
//    / \
//   b   c
//  / \ / \
// d  e f  g

#include <iostream>
using namespace std;

struct Node
{
    char data;
    Node *left;
    Node *right;
};

Node *newNode(char data)
{
    Node *node = new Node;
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

int search(char arr[], int start, int end, char value)
{
    for (int i = start; i <= end; i++)
    {
        if (arr[i] == value)
        {
            return i;
        }
    }
    return -1;
}

Node *buildTree(char in[], char pre[], int start, int end)
{
    static int preIndex = 0;
    if (start > end)
    {
        return NULL;
    }
    Node *node = newNode(pre[preIndex++]);
    if (start == end)
    {
        return node;
    }
    int inIndex = search(in, start, end, node->data);
    node->left = buildTree(in, pre, start, inIndex - 1);
    node->right = buildTree(in, pre, inIndex + 1, end);
    return node;
}

void printInorder(Node *node)
{
    if (node == NULL)
    {
        return;
    }
    printInorder(node->left);
    cout << node->data << " ";
    printInorder(node->right);
}

int main()
{
    char in[] = {'D', 'B', 'E', 'A', 'F', 'C', 'G'};
    char pre[] = {'A', 'B', 'D', 'E', 'C', 'F', 'G'};
    int n = sizeof(in) / sizeof(in[0]);
    Node *root = buildTree(in, pre, 0, n - 1);
    printInorder(root);
    return 0;
}