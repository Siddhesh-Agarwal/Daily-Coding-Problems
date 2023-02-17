// Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

// Given the root to such a tree, write a function to evaluate it.

// For example, given the following tree:

//     *
//    / \
//   +    +
//  / \  / \
// 3  2  4  5

// You should return 45, as it is (3 + 2) * (4 + 5).

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

int evaluate(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }
    if (root->left == NULL && root->right == NULL)
    {
        return root->data - '0';
    }
    int left = evaluate(root->left);
    int right = evaluate(root->right);
    if (root->data == '+')
    {
        return left + right;
    }
    else if (root->data == '-')
    {
        return left - right;
    }
    else if (root->data == '*')
    {
        return left * right;
    }
    else if (root->data == '/')
    {
        return left / right;
    }
}

/* Function to evaluate a tree */
int evaluate(Node *root)
{
    // empty tree
    if (!root)
        return 0;

    // leaf node i.e, an integer
    if (!root->left && !root->right)
        return root->data - '0';

    // evaluate left tree
    int l_val = evaluate(root->left);

    // evaluate right tree
    int r_val = evaluate(root->right);

    // check which operation to apply
    if (root->data == '+')
        return l_val + r_val;

    if (root->data == '-')
        return l_val - r_val;

    if (root->data == '*')
        return l_val * r_val;

    return l_val / r_val;
}

int main()
{
    Node *root = newNode('*');
    root->left = newNode('+');
    root->left->left = newNode('3');
    root->left->right = newNode('2');
    root->right = newNode('+');
    root->right->left = newNode('4');
    root->right->right = newNode('5');
    cout << "Result is: " << evaluate(root) << endl;
    return 0;
}