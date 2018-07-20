/** Node class for item in linked list. */
class Node {

    constructor(data){
    this.data = data;
    this.next = null;
    }
}


/** LinkedList class, keeping track of head and tail. */
class LinkedList {

    constructor(){
    this.head = null;
    this.tail = null;
    }

    /** LinkedList.append method -- add item at end of list. */
    append(data){
        let new_node = new Node(data);

        if (this.head === null) {
            this.head = new_node;
        }

        if (this.tail !== null) {
            this.tail.next = new_node;
        }

        this.tail = new_node;
    }

    /** LinkedList.print method -- print all items in list. */
    print(){
        let current = this.head;

        while (current !== null) {
            console.log(current.data);
            current = current.next;
        }
    }

    /** LinkedList.find method -- return true/false if data in list. */
    find(data){
        let current = this.head;

        while (current !== null) {
            
            if (current.data === data) {
                return true;
            }

            current = current.next;
        }

        return false;
    }

}


/* TEST CODE */

let ll = new LinkedList();

ll.append("apple");
ll.append("berry");
ll.append("cherry");

ll.print();

if (ll.find("berry")) {
    console.log("Found berry");
}

if (ll.find("durian")) {
    console.log("Found durian");
}


