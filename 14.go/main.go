package main

import (
	"fmt"
	"sort"
)

var x string = "全局变量"

// init
func init() {
	fmt.Println(hello()) // 必须有返回值
}

func hello() string {
	// fmt.Println("hello")
	return "hello"
}

// 结构体
type Student struct {
	name      string `json:"name"`
	pass_word string `json:"-"`
	// 结构体 tag    - 表示忽略
}

// 接口
type fu struct { // 定义可以写 type fuInterface struct{}
	name string
}

func (f fu) imple() {
	fmt.Println(f.name, "这是一个接口")
}

func imple(f fu) {
	f.imple()
}

// 泛型
func plus[T int | uint](n1, n2 T) T {
	return n1 + n2
}

func main() {
	/*
	   docker 轻量化虚拟机
	   消息队列
	   nsq  消息队列系统
	   监控和报警系统
	*/

	var name string
	name = "枫枫"
	fmt.Println(name)

	var age = 18
	fmt.Println(age)

	sex := "女" // 声明并赋值 短声明符号
	fmt.Println(sex)

	var a, b = 1, 2
	fmt.Println(a, b)

	var (
		s1 string = "hello"
		s3 int    = 3
	)
	fmt.Print(s1, s3) // 不换行输出

	const version = "1.0.0"

	fmt.Printf("%s 哇,你好美\n", "枫枫") // 格式化输出

	// 输入
	fmt.Println("请输入: ")
	var y string
	fmt.Scan(&y)
	fmt.Println(y)

	/*
	   fmt.Scan 本身定义就是返回 2 个值
	   之前写的是 fmt.Scan(&z)，没有用变量接收返回值，只是单纯调用函数，丢弃返回值，这是允许的
	   变量 := 函数() 就必须接收全部返回值，不能只接一部分
	*/
	fmt.Println("请输入: ")
	var z string
	n, err := fmt.Scan(&z)
	fmt.Println(n, err, age)

	// int int8 int32 int64 uint uint8 uint32 uint64
	// float32 float64
	// 单字节字符 byte == uint8
	// 多字节字符 rune

	// 想输出"" 用\
	fmt.Println("\"枫枫\"知道") // "枫枫"知道

	// 用` `就会直接输入内部的东西

	// 未赋值 输出默认值
	var n1 int
	var n2 bool
	var n3 string
	fmt.Printf("%#v\n", n1, n2, n3) // 0 false ""

	// 数组
	var lst [3]string = [3]string{"a", "b", "c"}
	fmt.Println(lst)
	fmt.Printf(lst[0])

	// 可以改值
	lst[0] = "1"

	var length = len(lst)
	fmt.Println(length)

	// 切片 slice
	var nlst []string
	nlst = append(nlst, "2")
	fmt.Println(nlst[:1])

	fmt.Println(nlst == nil) // 判空 返回boolean

	// 反c语法
	nameList := make([]string, 0)
	fmt.Println(nameList)

	sort.Strings(nameList)                                  // 正排 升序
	newNameList := sort.Reverse(sort.StringSlice(nameList)) // 降序
	fmt.Println(newNameList)

	// map 字典
	var dist map[int]string = map[int]string{
		1: "a",
		2: "b",
	}
	fmt.Println(dist[1]) // []写的是key
	delete(dist, 1)

	// if
	if dist[1] == "a" {
		fmt.Println("yes")
		return
	} // 推荐这种 最直接的 可写多个if

	// if, else, else if

	// 条件 && || !

	// 逻辑短路 一旦 多个条件 第一个就否了 后面的就不再执行了

	/* switch xxx {case fallthrough default}
	switch {
	case 1:
		...
		fallthrough    如果没有这个 当1命中时后边都不再执行了  默认使用了break
	case 2,3:
	default:
	}
	*/

	// 按住 ctrl alt shift 可选中多行同时输入一样的

	// for
	for i := 1; i <= 3; i++ {
		fmt.Println(i)
	}

	for {
		fmt.Println('1')
		break
	}

	for k, v := range dist {
		fmt.Println(k, v) // 循环切片
	}

	// 函数 func
	// 函数里不能写函数 只能用匿名函数
	var getName = func() string {
		return "枫枫"
	}
	fmt.Println(getName())

	// 闭包 设计一个函数 先传一个参数表示延时 后面再次传参数就是参数求和

	// 值传递 引用传递 引用和解引用* &

	// init函数 初始化

	// defer函数 延时函数
	defer func() {
		fmt.Println(recover())
	}()

	// 结构体
	stu := Student{name: "枫枫"}
	fmt.Println(stu)

	// 自定义数据类型

	// 类型别名

	// 接口
	f := fu{name: "接口"}
	f.imple()

	// 类型断言 xxx:=xxxx  返回boolean类型 instansof

	// 泛型

}

// 函数
func yes() bool {
	return true
}

func f1() (string, bool) {
	return "", true
}
