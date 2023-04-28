#include <iostream>

template <typename T>
class ArrayList {
private:
    T *data;
    int size;
    int length;
public:
    ArrayList() {
        this->length = 0;
        this->size = 5;
        this->data = new T[this->size];
    }
    void print() {
        std::cout << "[ ";
        for (int i = 0; i < this->len(); i++) {
            std::cout << this->data[i] << ' ';
        }
        std::cout << "]\n";
    }
    int len() {
        return this->length;
    }
    T get(int index) {
        if ((index >= 0) && (index < this->len())) {
            return this->data[index];
        }
    }
    void set(int index, T value) {
        if ((index >= 0) && (index < this->len())) {
            this->data[index] = value;
        } else if ((index == this->len()) && (index < this->size)) {
            this->data[index] = value;
            this->length++;
        } else if ((index == this->len()) && (index == this->size)) {
            T *data2 = new T[2 * this->size];
            for (int i = 0; i < this->len(); i++) {
                data2[i] = this->data[i];
            }
            data2[this->len()] = value;
            this->length++;
            this->size *= 2;
            delete[] this->data;
            this->data = data2;
        }
    }
    T del(int index) {
        if ((index >= 0) && (index < this->len())) {
            T deleted = this->data[index];
            for (int i = index; i < this->len(); i++) {
                this->data[i] = this->data[i + 1];
            }
            this->length--;
            return deleted;
        }
    }
    void append(T value) {
        this->set(this->len(), value);
    }
    T pop() {
        return this->del(this->len() - 1);
    }
    ~ArrayList() {
        delete[] this->data;
        this->data = nullptr;
    }
};

int main() {
    ArrayList<int> l;
    l.set(0, 1);
    l.set(1, 2);
    l.set(2, 3);
    l.set(3, 4);
    l.set(4, 5);
    l.set(5, 6);
    l.set(6, 7);
    l.print();
    l.del(2);
    l.del(2);
    l.del(2);
    l.del(2);
    l.del(0);
    l.del(0);
    l.del(0);
    l.print();
    l.append(99);
    l.print();
    l.pop();
    l.print();
    return 0;
}
