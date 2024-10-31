当前阶段仅针对单一场景进行程序化渲染工作。


## 使用方法

### 整体流程

+ 安装 Python 依赖，进入虚拟环境
+ 准备 Blender 环境
+ 设置程序选项
+ 运行 main.py

### 安装 Python 依赖

按照 requirements.txt 进行 pip 安装。

### 准备 Blender 环境

进入 `./src` 目录。

下载 `Reliance` 压缩文件，其中包括 `Assets` 和 `Addons` 两个文件。将 Reliance 文件解压到 `./src` 目录下。

当项目文件迁移到新的位置后，首先使用批处理命令 `reliance_checker.py` 文件进行依赖安装。这里要指定 Blender 的工作路径，例如：

```console
"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" asset00.blend -b -P reliance_checker.py
```

要注意这个脚本当中只涉及场景贴图素材的巡回，不会也不应该将插件安装到本地的 Blender-GUI 程序当中。

+ 之所以使用批处理命令进行贴图素材寻回，是因为 `Blender as python module` 无法正常使用 `save_as_mainfile` 方法，也不会返回正确的 `mainfile` 名称
+ 这里仍需要对不同版本的系统做适配。
