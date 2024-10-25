// App.js
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { TypeAnimation } from 'react-type-animation';
import CustomButton from './Button'; // Import your custom button
import { useEffect, useRef } from 'react';

function CameraPage() {
  const videoRef = useRef(null);

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      })
      .catch(err => console.error("Error accessing webcam:", err));
  }, []);

  return (
    <div>
      <h2>Camera View</h2>
      <video ref={videoRef} autoPlay />
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={
          <>
            <div className='animation-typing'>
              <TypeAnimation
                sequence={[
                  "Welcome to SLR", 
                  1000,
                  "Where learning ASL becomes easy",
                  1000
                ]}
                speed={20}
                repeat={Infinity}
                cursor={true}
                style={{ fontSize: '4em' }}
              />
            </div>
            <CustomButton /> {/* Your new colorful button */}
          </>
        } />
        <Route path="/camera" element={<CameraPage />} />
      </Routes>
    </Router>
  );
}

export default App;
