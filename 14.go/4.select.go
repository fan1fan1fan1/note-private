package main

import "sync"

var moneyChan1 = make(chan int)    // 声明并初始化一个长度为0的信道
var nameChan1 = make(chan string)  // 声明并初始化一个长度为0的信道
var doneChan = make(chan struct{}) // 声明一个用于关闭的信道

func send(name string, money int, wait *sync.WaitGroup) {
	moneyChan1 <- money
	nameChan1 <- name
	wait.Done()
}

func main() {
	// select 与 协程超时

	var wait sync.WaitGroup
	wait.Add(2)
	go send("张三", 2, &wait)
	go send("李四", 3, &wait)

	go func() {
		defer close(moneyChan1)
		defer close(nameChan1)
		defer close(doneChan)
		wait.Wait()
	}()

	var moneyList []int
	var nameList []string
	/*
		go func() {
			for money := range moneyChan1 {
				moneyList = append(moneyList, money)
			}
		}()

		for name := range nameChan1 {
			nameList = append(nameList, name)
		}
	*/
	for {
		select {
		case money := <-moneyChan1:
			moneyList = append(moneyList, money)
		case name := <-nameChan1:
			nameList = append(nameList, name)
		case <-doneChan:
			return
		}
	}

	// 协程超时处理

	// 线程安全问题处理办法 加锁 谁先抢到谁就把锁解开 这样另外的线程就用不了了
	// sync.Map

	/* 异常处理
	1.向上抛出
	2.中断
	3.恢复程序 重要
	*/
}
