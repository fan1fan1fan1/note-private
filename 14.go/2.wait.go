package main

import (
	"sync"
)

// 协程
var wait sync.WaitGroup

func shopping(name string, wait *sync.WaitGroup) {
	wait.Done()
}

func main() {
	// 协程 重要 可以同时做两个任务线
	// 如果是单线程加函数运行 当主进程执行完毕时 子函数可能强制结束
	var wait sync.WaitGroup
	wait.Add(2)
	go shopping("张三", &wait)
	go shopping("李四", &wait)
	wait.Wait()
}
