# wuyi-node

此项目主要是为了检测并搜集单机上的健康状态信息，并通过api接口的方式暴露给master node机器。

## Quick Start

### 1. Installation

```shell script
pip install -r requirments.txt
```
### 2. Write the specific code

此步骤需要你在`app.py`对应的函数中编写搜集节点信息的代码.

如果需要将代码融入到自己的项目当中，只需要将app.py复制过去，并调用`run_server`函数即可。

### 3. Run the code

```shell script
chmod +x run.sh
./run.sh
```
