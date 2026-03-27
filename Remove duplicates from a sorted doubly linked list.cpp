class Solution {
public:
    Node* removeDuplicates(Node* head) {

        if (!head) return head;

        Node* curr = head;

        while (curr && curr->next) {
            if (curr->data == curr->next->data) {

                Node* nextNode = curr->next->next;

                delete curr->next;

                curr->next = nextNode;
                if (nextNode) nextNode->prev = curr;

            } else {
                curr = curr->next;
            }
        }

        return head;
    }
};