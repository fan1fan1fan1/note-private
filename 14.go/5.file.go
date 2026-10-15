package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	// 一 文件读取
	// 1.一次性读取全部
	byteData, err := os.ReadFile("FILE.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(byteData))

	// 2.分片读取
	file, err := os.Open("14.go/FILE.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	for {
		var byteData = make([]byte, 13)
		n, err := file.Read(byteData)
		if err != nil {
			if err == io.EOF { // 读完了
				break
			}
		}
		fmt.Println(string(byteData[:n]))
		fmt.Println(string(byteData), n)
	}

	// 3.带缓冲读 指定按行读
	file1, err1 := os.Open("14.go/FILE.txt")
	if err1 != nil {
		panic(err1)
	}
	defer file1.Close()
	buf := bufio.NewReader(file1)
	for {
		line, _, err2 := buf.ReadLine()
		if err2 == io.EOF {
			break
		}
		fmt.Println(string(line), err2)
	}

	// 4.指定分隔符 eg.根据空格读取
	file2, err2 := os.Open("14.go/FILE.txt")
	if err2 != nil {
		panic(err2)
	}
	defer file2.Close()
	buf2 := bufio.NewScanner(file2)
	buf2.Split(bufio.ScanWords)
	var index int
	for buf2.Scan() {
		// 如果for循环判断条件未true 就继续读
		index++
		fmt.Println(index, buf2.Text())
	}

	// 二 文件写入
	file3, err3 := os.OpenFile("14.go/FILE.txt", os.O_RDONLY, 0666)
	// os.O_CREATE 只写 如果此时用read方法会报错   os.O_RDONLY只读 os.O_RDWR可读可写
	// perm 只作用于linux系统使用时
	if err3 != nil {
		panic(err3)
	}
	defer file3.Close()
	file3.Write([]byte("你好"))

	// 三 文件复制   io.Copy(file1,file2)

	// 四 目录操作   读取文件夹里的内容
	// os.ReadDir("./") // 当前路径
	dir, err4 := os.ReadDir("14.go")
	if err4 != nil {
		fmt.Println(err4)
		return
	}
	for _, entry := range dir {
		info, _ := entry.Info()

		fmt.Println(entry.IsDir(), entry.Name(), info.Size())
	}

}
