# -*- coding: utf-8 -*-
"""
Desc: 意图识别模型 - 独立 Flask API 服务
     不修改训练代码，单独提供对外接口
"""
import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

# 解决项目路径导入问题（必须加）
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# 初始化 Flask
app = Flask(__name__)
CORS(app)  # 允许跨域

# 全局加载模型（服务启动时加载一次，性能最优）
predictor = None

def load_model():
    """加载训练好的模型（从原文件导入推理类）"""
    global predictor
    try:
        from text_classify.deploy.jit_predictor import Predictor
        predictor = Predictor(
            jit_model_path="./output/intention/bert1/models/best.pt"
        )
        print("✅ 意图识别模型加载完成！")
    except Exception as e:
        print(f"❌ 模型加载失败：{e}")
        raise e

# ------------------- API 接口 -------------------
@app.route("/api/intent/recognize", methods=["POST"])
def recognize_intent():
    """意图识别核心接口"""
    try:
        data = request.get_json()
        # 把前端通过 POST 请求传过来的 JSON 数据，解析成 Python 能直接用的字典。
        if not data or "text" not in data:
            return jsonify({"code": 400, "msg": "缺少参数 text", "data": None})

        text = data["text"].strip()
        top_k = data.get("top_k", 3)

        # 调用模型推理
        result = predictor.predict(text, k=top_k)

        return jsonify({
            "code": 200,
            "msg": "识别成功",
            "data": {
                "input": text,
                "result": result
            }
        })
    except Exception as e:
        return jsonify({"code": 500, "msg": f"服务错误：{str(e)}", "data": None})

# ------------------- 启动服务 -------------------
if __name__ == '__main__':
    load_model()
    # 0.0.0.0 允许外网访问，端口 5000
    app.run(host="0.0.0.0", port=5000, debug=False)