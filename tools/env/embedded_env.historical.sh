#!/bin/bash
# 历史环境脚本，来源 embedded-learning@ad4e5f15732bade382888a7711dd5685b73b409a / .embedded_env
# 仅供复用参考；原安装路径不代表当前环境，当前工具链以 hardware 的入口文档为准。
# 本文件不参与自动环境加载；source 会修改当前 shell 的 PATH。
if command -v arm-none-eabi-gcc >/dev/null 2>&1; then
  :
else
  export PATH=/usr/local/arm-gcc/bin:$PATH
fi
echo "✅ Embedded ARM environment loaded"
if command -v arm-none-eabi-gcc >/dev/null 2>&1; then
  echo "   $(arm-none-eabi-gcc --version | head -1)"
else
  echo "   arm-none-eabi-gcc not found in PATH"
fi
