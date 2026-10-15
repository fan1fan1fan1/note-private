package main

import (
	"fmt"
	"os"
	"testing"
)

// 1.单元测试 测试

func ADD(n1, n2 int) int {
	return n1 + n2
}

// 一般的测试文件 就是被测试文件名_test

func TestADD(t *testing.T) {
	res := ADD(1, -1)
	if res != 0 {
		t.Errorf("测试失败")
		return
	}
	t.Logf("测试通过")
}

// 在终端输入 go test 测试文件文件名 运行
// go test 文件名 -v  输出详细信息

// 2.子测试
func TestADD2(t *testing.T) {
	t.Run("add1", func(t *testing.T) {
		res := ADD(1, -1)
		if res != 0 {
			t.Errorf("测试失败")
			return
		}
	})
	t.Run("add2", func(t *testing.T) {
		res := ADD(1, 1)
		if res != 2 {
			t.Errorf("测试失败")
			return
		}
	})

	t.Logf("测试通过")
}

// 子测试里Fatal不终止程序

// 3.多用例测试 循环
func TestADD3(t *testing.T) {
	cases := []struct {
		name           string
		A, B, Expected int
	}{
		{"a1", 2, 3, 5},
		{"a2", 2, -3, -1},
		{"a3", 2, 0, 2},
	}
	for _, s := range cases {
		t.Run(s.name, func(t *testing.T) {
			if ADD(s.A, s.B) != s.Expected {
				t.Errorf("测试失败")
				return
			}
		})
	}

	t.Logf("测试通过")
}

// 4.test main  测试入口 比如连接了数据库 文件
func setup() {
	fmt.Println("before")
}

func teardown() {
	fmt.Println("after")
}

func TestADD4(t *testing.T) {
	fmt.Println("test4")
}
func TestADD5(t *testing.T) {
	fmt.Println("test5")
}

func TestMain(m *testing.M) { // 类似生命周期
	fmt.Println("TestMain")

	setup()
	code := m.Run()
	teardown()

	os.Exit(code)
}
