1.安装 ollama -v 

2.复制模型名称到命令行    ollama + pull(run) + 模型名称

3.下载模型

	模型越大 执行效率越高 答案越精准

4.使用模型

5.命令介绍   命令行ollama 回车

	ollama list    显示全部已下载模型
	ollama show    显示模型信息
	ollama pull    负责单个模型的下载和更新(拉取最新模型)
	ollama run + 模型名称     开始执行模型 输入问题
		使用三个引号进行对话"""    意味着进行多行对话 输入较多内容
		
	ollama run + 模型名称 + -version    执行结果后 显示执行效率

6.将ollama与n8n‘结合 

	1.n8n中找 http request
	
	1.url中填写ollama的api地址
	如果ollama和n8n在同一个机器上 http://localhost:11434/api/generate 
	不同机器 替换为ollama所在机器的ip和端口
	（如  http://192.168.1.100:11434/api/generate  ，需确保网络可通 ）
	
	3.方法 POST
	
	4.Body内容 (json)
	{
		     "model": "mistral", // 替换为你实际运行的 Ollama 模型名称，
		  比如 "llama3" "deepseek" 等
		    "prompt": "你好，用简洁的语言介绍下 AI 趋势", // 替换为你要让
		  模型执行的提示词
		    "stream": false // 设为 false 以获取完整响应，若需流式输出可
		  设为 true
	}
	
	5.测试节点 点击save n8n会向ollama发送请求 输出
