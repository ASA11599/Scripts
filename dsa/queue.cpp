template <typename T>
class Queue {
    private:
    std::vector<T> items;
    std::mutex lock;
    public:
    void enqueue(T item);
    T dequeue();
    int size();
};

template <typename T>
int Queue<T>::size() {
    return this->items.size();
}

template <typename T>
void Queue<T>::enqueue(T item) {
    std::lock_guard<std::mutex> lg(this->lock);
    this->items.push_back(item);
}

template <typename T>
T Queue<T>::dequeue() {
    if (this->size() > 0) {
        T item = this->items[0];
        std::lock_guard<std::mutex> lg(this->lock);
        this->items.erase(this->items.begin());
        return item;
    } else {
        throw "Queue empty";
    }
}
