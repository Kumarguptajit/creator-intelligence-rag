"use client";

import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { Eye, ThumbsUp, MessageCircle, TrendingUp } from "lucide-react";


export default function Home() {
  const [videoA, setVideoA] = useState("");
  const [videoB, setVideoB] = useState("");
  const [question, setQuestion] = useState("");

  const [videoData, setVideoData] =
    useState<any>(null);

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Paste two videos and click Compare."
    }
  ]);
  const winnerViews =
    videoData &&
    videoData.video_a.views >
    videoData.video_b.views;

  const winnerLikes =
    videoData &&
    videoData.video_a.likes >
    videoData.video_b.likes;

  const winnerComments =
    videoData &&
    videoData.video_a.comments >
    videoData.video_b.comments;

  const winnerEngagement =
    videoData &&
    videoData.video_a.engagement_rate >
    videoData.video_b.engagement_rate;

  async function compareVideos() {
    setMessages([
      {
        role: "assistant",
        content: "Analyzing videos..."
      }
    ]);

    const res = await fetch(
      "http://127.0.0.1:8000/compare",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          video_a_url: videoA,
          video_b_url: videoB,
        }),
      }
    );

    const text = await res.text();
    const contextRes = await fetch(
      "http://127.0.0.1:8000/comparison-context"
    );

    const contextData =
      await contextRes.json();

    setVideoData(
      contextData
    );

    setMessages([
      {
        role: "assistant",
        content: text
      }
    ]);
  }

  async function askQuestion() {

    const userQuestion = question;

    setQuestion("");

    setMessages([
      ...messages,
      {
        role: "user",
        content: userQuestion
      },
      {
        role: "assistant",
        content: ""
      }
    ]);

    const res = await fetch(
      "http://127.0.0.1:8000/stream",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          question: userQuestion
        })
      }
    );

    const reader = res.body?.getReader();

    const decoder = new TextDecoder();

    let answer = "";

    while (true) {

      const { done, value } =
        await reader!.read();

      if (done) break;

      answer += decoder.decode(
        value
      );

      setMessages(prev => {

        const updated = [...prev];

        updated[
          updated.length - 1
        ] = {
          role: "assistant",
          content: answer
        };

        return updated;
      });

    }

  }

  const inputClass = "rounded-3xl border border-slate-300 bg-slate-50 px-4 py-3 shadow-sm outline-none transition placeholder:text-slate-500 focus:border-blue-400 focus:ring-2 focus:ring-blue-100 text-slate-900 w-full";
  const urlInputAClass = `${inputClass} ${videoA.trim().startsWith("http") ? "text-sky-900" : "text-slate-900"}`;
  const urlInputBClass = `${inputClass} ${videoB.trim().startsWith("http") ? "text-sky-900" : "text-slate-900"}`;
  const buttonClass = "rounded-3xl bg-slate-900 px-6 py-3 text-sm font-semibold text-white shadow hover:bg-slate-800 transition w-full md:w-auto";
  const cardBaseClass = "rounded-[1.75rem] border p-5 shadow-sm w-full";
  const statClass = "rounded-2xl border border-slate-200 bg-slate-50 p-3 text-slate-800 shadow-sm";
  const statLabelClass = "text-xs uppercase tracking-[0.12em] text-slate-500";
  const assistantMessageClass = "rounded-[2rem] border border-slate-200 bg-sky-600 p-8 shadow-sm text-white";
  const defaultMessageClass = "rounded-[2rem] border border-slate-200 bg-white p-8 shadow-sm";
  const assistantMarkdownClass = "prose prose-invert space-y-6 max-w-none text-white prose-p:leading-relaxed prose-li:my-2";
  const defaultMarkdownClass = "prose prose-slate space-y-4 max-w-none prose-p:leading-relaxed prose-li:my-2";

  return (
    <main className="min-h-screen bg-slate-100 py-8">
      <div className="mx-auto w-full max-w-4xl px-4 sm:px-6">
        <div className="overflow-hidden rounded-[2rem] border border-sky-200 bg-sky-50 p-6 sm:p-8 shadow-xl">
          <h1 className="text-4xl font-bold tracking-tight text-slate-900">
            Creator's Intelligent Assistant
          </h1>
          <p className="mt-3 max-w-2xl text-sm text-slate-600">
            Compare two creator videos side by side, then ask follow-up questions about the comparison.
          </p>

          <div className="mt-8 grid gap-4 sm:grid-cols-[1fr_auto] sm:items-end">
            <div className="grid gap-4">
              <input
                className={urlInputAClass}
                placeholder="First Video URL"
                value={videoA}
                onChange={(e) => setVideoA(e.target.value)}
              />
              <input
                className={urlInputBClass}
                placeholder="Second Video URL"
                value={videoB}
                onChange={(e) => setVideoB(e.target.value)}
              />
            </div>
            <button onClick={compareVideos} className={buttonClass}>
              Compare Videos
            </button>
          </div>

          <div className="mt-4 grid gap-4 sm:grid-cols-[1fr_auto] sm:items-end">
            <input
              className={inputClass}
              placeholder="Ask a question..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
            />
            <button onClick={askQuestion} className={buttonClass}>
              Send
            </button>
          </div>
        </div>

        {videoData && (
          <div className="mt-8 grid gap-4 sm:grid-cols-2">
            <div className={`${cardBaseClass} ${winnerEngagement ? "bg-emerald-50 border-emerald-200" : "bg-orange-50 border-orange-200"}`}>              {videoData.video_a.thumbnail && (
                <img
                  src={videoData.video_a.thumbnail}
                  alt={videoData.video_a.title}
                  className="mb-4 h-32 w-full rounded-lg object-cover"
                />
              )}              <div className={`mb-4 h-1.5 rounded-full ${winnerEngagement ? "bg-emerald-500/30" : "bg-orange-500/30"}`} />
              <div className="mb-4">
                <h2 className="text-xl font-semibold text-slate-900">First Video</h2>
                <p className="mt-1 text-sm text-slate-500">
                  {videoData.video_a.creator}
                </p>

                <p className="text-sm text-slate-500">
                  Followers: {videoData.video_a.follower_count || "N/A"}
                </p>
              </div>

              <div className="mb-4">
                <div className="font-semibold text-slate-900">{videoData.video_a.title}</div>
              </div>

              <div className="grid gap-4 sm:grid-cols-2">
                <div className={statClass}>
                  <div className="flex items-center gap-2">
                    <Eye size={16} className="text-slate-600" />
                    <div className={statLabelClass}>Views</div>
                  </div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">{videoData.video_a.views?.toLocaleString()}</div>
                </div>
                <div className={statClass}>
                  <div className="flex items-center gap-2">
                    <ThumbsUp size={16} className="text-slate-600" />
                    <div className={statLabelClass}>Likes</div>
                  </div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">{videoData.video_a.likes?.toLocaleString()}</div>
                </div>
                <div className={statClass}>
                  <div className="flex items-center gap-2">
                    <MessageCircle size={16} className="text-slate-600" />
                    <div className={statLabelClass}>Comments</div>
                  </div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">{videoData.video_a.comments?.toLocaleString()}</div>
                </div>
                <div className={statClass}>
                  <div className="flex items-center gap-2">
                    <TrendingUp size={16} className="text-slate-600" />
                    <div className={statLabelClass}>Engagement</div>
                  </div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">{videoData.video_a.engagement_rate}%</div>
                </div>
                <div className={statClass}>
                  <div className={statLabelClass}>Duration</div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">
                    {Math.floor(videoData.video_a.duration / 60)}m {videoData.video_a.duration % 60}s
                  </div>
                </div>
              </div>
            </div>

            <div className={`${cardBaseClass} ${winnerEngagement ? "bg-orange-50 border-orange-200" : "bg-emerald-50 border-emerald-200"}`}>              
              {videoData.video_b.thumbnail && (
                <img
                  src={videoData.video_b.thumbnail}
                  alt={videoData.video_b.title}
                  className="mb-4 h-32 w-full rounded-lg object-cover"
                  onError={(e) => {
                    e.currentTarget.style.display = "none";
                  }}
                />
              )}              
              <div className={`mb-4 h-1.5 rounded-full ${winnerEngagement ? "bg-orange-500/30" : "bg-emerald-500/30"}`} />
              <div className="mb-4">
                <h2 className="text-xl font-semibold text-slate-900">Second Video</h2>
                <p className="mt-1 text-sm text-slate-500">{videoData.video_b.creator}</p>
                <p className="text-sm text-slate-500">
                  Followers: {videoData.video_b.follower_count || "N/A"}
                </p>
              </div>

              <div className="mb-4">
                <div className="font-semibold text-slate-900">{videoData.video_b.title}</div>
              </div>

              <div className="grid gap-4 sm:grid-cols-2">
                <div className={statClass}>
                  <div className="flex items-center gap-2">
                    <Eye size={16} className="text-slate-600" />
                    <div className={statLabelClass}>Views</div>
                  </div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">{videoData.video_b.views?.toLocaleString()}</div>
                </div>
                <div className={statClass}>
                  <div className="flex items-center gap-2">
                    <ThumbsUp size={16} className="text-slate-600" />
                    <div className={statLabelClass}>Likes</div>
                  </div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">{videoData.video_b.likes?.toLocaleString()}</div>
                </div>
                <div className={statClass}>
                  <div className="flex items-center gap-2">
                    <MessageCircle size={16} className="text-slate-600" />
                    <div className={statLabelClass}>Comments</div>
                  </div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">{videoData.video_b.comments?.toLocaleString()}</div>
                </div>
                <div className={statClass}>
                  <div className="flex items-center gap-2">
                    <TrendingUp size={16} className="text-slate-600" />
                    <div className={statLabelClass}>Engagement</div>
                  </div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">{videoData.video_b.engagement_rate}%</div>
                </div>
                <div className={statClass}>
                  <div className={statLabelClass}>Duration</div>
                  <div className="mt-2 text-xl font-semibold text-slate-900">
                    {Math.floor(videoData.video_b.duration / 60)}m {videoData.video_b.duration % 60}s
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        <div className="mt-8 space-y-4">
          {messages.map((message, index) => (
            <div key={index} className={message.role === "assistant" ? assistantMessageClass : defaultMessageClass}>
              <div className="mb-3 flex items-center gap-3 text-sm uppercase tracking-[0.2em] text-slate-200">
                <span>{message.role}</span>
              </div>
              <div className={message.role === "assistant" ? assistantMarkdownClass : defaultMarkdownClass}>
                <ReactMarkdown>{message.content}</ReactMarkdown>
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}