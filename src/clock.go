package main

import (
	"fmt"
	"time"
)

type Clock struct {
	hours, minutes, seconds int
}

func (this *Clock) Tick() {
	this.seconds++
	if this.seconds == 60 {
		this.seconds = 0
		this.minutes++
	}
	if this.minutes == 60 {
		this.minutes = 0
		this.hours++
	}
	if this.hours == 24 {
		this.hours = 0
	}
}

func (this *Clock) String() string {
	sString := fmt.Sprintf("%d", this.seconds)
	if len(sString) == 1 {
		sString = "0" + sString
	}
	mString := fmt.Sprintf("%d", this.minutes)
	if len(mString) == 1 {
		mString = "0" + mString
	}
	hString := fmt.Sprintf("%d", this.hours)
	if len(hString) == 1 {
		hString = "0" + hString
	}
	return hString + ":" + mString + ":" + sString
}

func (this *Clock) Start() <-chan Clock {
	clockChan := make(chan Clock)
	go func(c chan<- Clock) {
		for {
			this.Tick()
			c <- *this
			time.Sleep(time.Second)
		}
	}(clockChan)
	return clockChan
}

func main() {
	var c Clock = Clock{23, 59, 55}
	cChan := c.Start()
	for i := 0; i < 10; i++ {
		current := <-cChan
		fmt.Println(current.String())
	}
}
