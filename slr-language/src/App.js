import {TypeAnimation} from 'react-type-animation'

function App() {
  return (
    <div className='animation-typing'>
    <TypeAnimation
        sequence={[
            "Welcome to SLR", 
            1000,
            "Where learning ASL becomes easy",
            1000
        ]}
        speed ={20}
        repeat={Infinity}
        cursor={true}
        style = {{fontSize: '4em'}}
        />
        </div>
    
  );
}

export default App;
