import React, { useState, useEffect } from 'react';
import './Home.css';
import { googleLogout } from '@react-oauth/google';
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();
  const [user, setUser] = useState();
  const [data, setData] = useState([]);

  function handleLogout() {
    googleLogout();
    setUser({});
    console.log("Logged out successfully!");
    navigate("/");
  }

  const handleReply = (index) => {
    const updatedData = [...data];
    updatedData[index].isReplying = true;
    setData(updatedData);
  };

  const handleBack = (index) => {
    const updatedData = [...data];
    updatedData[index].isReplying = false;
    setData(updatedData);
  };

  const handleSubmitReply = async (index) => {
    const replyContent = document.querySelector(`#replyText${index}`).value;
    if (replyContent.trim() !== '') {
      const response = await fetch(`/reviews/${index}/reply`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ reply_content: replyContent }),
      });

      if (response.ok) {
        const updatedData = [...data];
        updatedData[index].replies.push(replyContent);
        updatedData[index].isReplying = false;
        setData(updatedData);
      } else {
        console.error('Failed to submit reply');
      }
    }
  };

  useEffect(() => {
    fetch("/reviews")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
      });
  }, []);

  return (
    <div className="app-container">
      <header>
        <h1>My Reviews</h1>
        <button onClick={handleLogout} className="logout-button">
          Logout
        </button>
      </header>
      {data.length === 0 ? (
        <h2>
          <center>Loading...</center>
        </h2>
      ) : (
        data.map((review, i) => (
          <div key={i} className="review-container">
            <div className="review-header">
              <div className="user-avatar">
                {review.photo_url ? (
                  <img
                    src={review.photo_url}
                    alt={review.name}
                    className="avatar-img"
                  />
                ) : (
                  <div className="default-avatar">👤</div>
                )}
              </div>
              <div className="user-details">
                <p>
                  <strong>{review.name}</strong>
                </p>
                <p className="review-date">{review.date}</p>
              </div>
            </div>
            <div className="star-rating">
              {[...Array(review.stars).keys()].map((star, j) => (
                <span key={j}>&#9733;</span>
              ))}
              {review.stars % 1 !== 0 && <span>&#9734;</span>}
            </div>
            <p className="review-content">{review.content}</p>
            {review.isReplying ? (
              <div className="reply-section">
                <button onClick={() => handleBack(i)} className="reply-button">
                  Back
                </button>
                <textarea
                  id={`replyText${i}`}
                  placeholder="Type your reply..."
                  className="reply-textarea"
                />
                <button
                  onClick={() => handleSubmitReply(i)}
                  className="reply-button"
                >
                  Submit
                </button>
              </div>
            ) : (
              <button onClick={() => handleReply(i)} className="reply-button">
                Reply
              </button>
            )}
            {review.replies && review.replies.length > 0 && (
              <div className="replies-section">
                <strong>Replies:</strong>
                <ul>
                  {review.replies.map((reply, j) => (
                    <li key={j} className="reply-item">
                      {reply}
                    </li>
                  ))}
                </ul>
              </div>
            )}
            <hr />
          </div>
        ))
      )}
    </div>
  );
}

export default Home;
