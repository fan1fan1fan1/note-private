package main

import "sync"

// 信道 channel
var moneyChan = make(chan int) // chan 类型 信道
func pay(name string, money int, wait *sync.WaitGroup) {
	moneyChan <- money
	wait.Done()
}
func main() {
	// channel 信道

	var wait sync.WaitGroup
	wait.Add(2)
	go pay("张三", 2, &wait)
	go pay("李四", 3, &wait)

	go func() {
		defer close(moneyChan)
		wait.Wait()
		// close(moneyChan)   可以写成 ↑

	}()

	for {
		//money := <-moneyChan
		money, ok := <-moneyChan
		if !ok {
			break
		}
		_ = money
	}
	// for里如果传一个参数 直接就是值chan int
	// 如果是两个参数 第二个判断 true表示能拿

	// ↑ 可以写成
	/*
		var moneyList []int
		for money := range moneyChan{
			moneyList = append(moneyList, money)
		}
	*/

	wait.Wait()
}
