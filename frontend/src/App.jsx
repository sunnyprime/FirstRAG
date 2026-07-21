import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [asking, setAsking] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a PDF first.");
      return;
    }

    try {
      setLoading(true);
      setMessage("");

      const formData = new FormData();

      formData.append("file", file);

      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error("PDF upload failed");
      }

      setMessage(
        `${data.filename} uploaded successfully. ${data.stored_chunks} chunks stored.`,
      );
    } catch (error) {
      console.error(error);
      setMessage("Something went wrong while uploading the PDF.");
    } finally {
      setLoading(false);
    }
  };

  const handleAsk = async () => {
    if (!question.trim()) {
      setAnswer("Please enter a question.");
      return;
    }

    try {
      setAsking(true);
      setAnswer("");

      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error("Failed to get answer");
      }

      setAnswer(data.answer);
    } catch (error) {
      console.error(error);

      setAnswer("Something went wrong while getting the answer.");
    } finally {
      setAsking(false);
    }
  };

  return (
    <div>
      <h1>My First RAG Application</h1>

      <h2>Upload PDF</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(event) => {
          setFile(event.target.files[0]);
        }}
      />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload PDF"}
      </button>

      {message && <p>{message}</p>}
      <hr />

      <h2>Ask About Your PDF</h2>

      <input
        type="text"
        placeholder="Ask something about your document..."
        value={question}
        onChange={(event) => {
          setQuestion(event.target.value);
        }}
      />

      <button onClick={handleAsk} disabled={asking}>
        {asking ? "Thinking..." : "Ask"}
      </button>

      {answer && (
        <div>
          <h3>AI Answer</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;
