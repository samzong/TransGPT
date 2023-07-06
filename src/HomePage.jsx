import { useState } from "react";
import { Input, Button, Select } from "antd";

const { Option } = Select;

const HomePage = () => {
  const [currentLanguage, setCurrentLanguage] = useState("en");
  const [documentUrl, setDocumentUrl] = useState("");
  const [translationResult, setTranslationResult] = useState("");

  const params = {
    current_language: 'en',
    document_url: 'https://raw.githubusercontent.com/openai/openai-cookbook/main/how_to_work_with_large_language_models.md'
  };

  const handleTranslate = () => {
    // 调用后端 API 进行翻译
      fetch(`http://127.0.0.1:8000/translate?${new URLSearchParams(params)}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        mode: "no-cors",
      })
        .then((response) => response.json())
        .then((data) => {
          setTranslationResult(data.translation);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    };

  return (
    <div style={{ background: "white", padding: "20px" }}>
      <h1 style={{ textAlign: "center", marginBottom: "20px" }}>自动翻译 markdown 文件</h1>
      <div style={{ display: "flex", justifyContent: "center", marginBottom: "20px" }}>
        <Select
          defaultValue={currentLanguage}
          onChange={(value) => setCurrentLanguage(value)}
          style={{ marginRight: "20px", width: "200px" }}
        >
          <Option value="en">英文</Option>
          <Option value="zh">中文</Option>
        </Select>
        <Input
          placeholder="请输入文档URL"
          value={documentUrl}
          onChange={(e) => setDocumentUrl(e.target.value)}
          style={{ width: "600px" }}
        />
        <Button type="primary" onClick={handleTranslate} style={{ marginLeft: "20px" }}>
          翻译
        </Button>
      </div>
      <textarea
        value={translationResult}
        readOnly
        rows={30}
        cols={100}
        style={{ width: "900px", height: "600px", overflow: "auto" }}
      />
    </div>
  );
};

export default HomePage;
