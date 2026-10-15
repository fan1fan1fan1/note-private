package main

import (
	"fmt"
	"reflect"
	"strings"
)

// 1.类型判断 获取类型
func getType(obj any) {
	t := reflect.TypeOf(obj)
	switch t.Kind() {
	case reflect.String:
		fmt.Println("string")
	case reflect.Int:
		fmt.Println("int")
	}
}

// 2.通过反射获取实际值
func getValue(obj any) {
	v := reflect.ValueOf(obj)
	switch v.Kind() {
	case reflect.String:
		fmt.Println("string", v.String())
	case reflect.Int:
		fmt.Println("int", v.Int())
	}
}

// 3.通过反射修改值
func setValue(obj any, value any) {
	v1 := reflect.ValueOf(obj)
	v2 := reflect.ValueOf(value)
	fmt.Println(v1.Elem(), v2.Elem()) // 需要解指针
	if v1.Elem().Kind() != v2.Kind() {
		return
	}
	v1 = v1.Elem()
	switch v1.Kind() {
	case reflect.String:
		v1.SetString(value.(string))
	case reflect.Int:
		v1.SetInt(int64(value.(int)))
		v2.SetInt(v2.Int())
	}
}

// 4.结构体反射
type student struct {
	name string `json:"name"`
	age  int    `json:"age"`
}

func parseJson(obj any) {
	v := reflect.ValueOf(obj)
	t := reflect.TypeOf(obj)
	for i := 0; i < v.NumField(); i++ {
		tf := t.Field(i)
		jsonTag := tf.Tag.Get("json")
		if jsonTag == "-" {
			continue
		}
		if jsonTag == "" {
			jsonTag = tf.Name
		}
		fmt.Println("%s,%#v\n", tf.Name, jsonTag)
		fmt.Println(jsonTag, v.Field(i).Interface())
	}
}

type User struct {
	name1 string `big:"-"`
	name2 string
}

func setStruct(obj any) {
	v := reflect.ValueOf(obj).Elem()
	t := reflect.TypeOf(obj).Elem()
	for i := 0; i < v.NumField(); i++ {
		value := v.Field(i)
		fmt.Println(value)
		big := t.Field(i).Tag.Get("big")
		if big == "-" {
			continue
		}
		value.SetString(strings.ToUpper(value.String()))
	}
}

type User1 struct{}

func (User1) Call() {
	fmt.Println("call")
}

func Call(obj any) {
	v := reflect.ValueOf(obj).Elem()
	t := reflect.TypeOf(obj).Elem()
	for i := 0; i < v.NumMethod(); i++ {
		m := t.Method(i)
		fmt.Println(m.Name)
		if m.Name == "Call" {
			continue
		}
		method := v.Method(i)
		method.Call([]reflect.Value{reflect.ValueOf("xx")})
	}
}

func main() {
	// 反射
	// 1.类型判断 获取类型
	getType(2)
	getType("a")

	// 2.通过反射获取实际值
	getValue("a")
	getValue(1)

	// 3.通过反射修改值
	var name = '1'
	var age = 20
	setValue(&name, '2')
	setValue(&age, 25) // 有关set改变 修改 都需要&
	fmt.Println(name, age)

	// 4.结构体反射
	// eg.读取json值
	s := student{name: "x", age: 20}
	parseJson(s)

	// eg.修改结构体值
	s1 := User{name1: "a", name2: "b"}
	setStruct(s1)
	fmt.Println(s1)

	// eg.调用结构体方法
	s2 := User1{}
	Call(&s2)

	// 网络编程

	// go部署
	/*
		go build
		go build xxx.go            main
		go build main.exe xxx.go   强制重命名
	*/

	// 交叉编译  windows和linux
	/*
		新建一个build.bat 写:
		set CGO_ENABLED = 0
		set GOOS = linux
		set GOARCH = amd64


		执行go build -o main main.go

		建议golang软件底部终端->设置->tools->terminal->shell path改成cmd.exe

		然后打包go build
		文件可上传至linux 增加可执行权限 即可

	*/
}
