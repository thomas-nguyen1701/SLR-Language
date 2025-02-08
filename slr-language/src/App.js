// App.js
import {lazy, Suspense} from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { TypeAnimation } from 'react-type-animation';
import { CustomButton } from './Button.js'; // import custom button from Button.js
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
      .catch(err => console.error("Error accessing webcam: ", err));
  }, []);

  return (
    <div>
      <video ref={videoRef} autoPlay />
    </div>
  );
}

function App() {
  return (
    <Router>
         <Suspense fallback={<div className="container">Loading...</div>}>
      <Routes>
        <Route path="/" element={
          <>
            <div className='animation-typing'>
              <TypeAnimation
                sequence={[
                  "Welcome to SLR.", 
                  1000,
                  "Where learning ASL becomes easy.",
                  1000
                ]}
                speed={20}
                repeat={Infinity}
                cursor={true}
              />
            </div>
            <CustomButton /> 
          </>
        } />
        <Route path="/camera" element={<CameraPage />} />
      </Routes>
      </Suspense>
    </Router>
  );
}

export default App;
