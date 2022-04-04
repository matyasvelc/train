import React, { useEffect } from 'react'
import ReactDOM from 'react-dom'
import Progress from './lib/progress'
import './styles.css'
import Slider, { Range } from 'rc-slider';
import 'rc-slider/assets/index.css';
import pozadi from './nosignal.gif'
import vlak from './train.svg'

async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

const style = { float: 'left', width: 160, height: 200, marginBottom: 160, marginLeft: 50 };
const parentStyle = { overflow: 'hidden' };

const marks = {
  '-50': {
    style: {
      color: 'red',
    },
    label: <strong>-50</strong>,
  },
  0: {
    style: {
      color: 'red',
    },
    label: <strong>0</strong>,
  },
  50: {
    style: {
      color: 'red',
    },
    label: <strong>50</strong>,
  },
};

function App() {
  const [temp, setTemp] = React.useState()
  const [rpm, setRpm] = React.useState()
  const [speed, setSpeed] = React.useState()
  const [svetlo, setSvetlo] = React.useState()
  const [rychlost, setRychlost] = React.useState()

  useEffect(() => {
    const timer = setInterval(() => {
      fetch('http://127.0.0.1:5000/getSpeed')
        .then(res => {
          return res.json();
        })
        .then(data => {
          setSpeed(data.speed);
        });
    }, 1000);
    
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      fetch('http://127.0.0.1:5000/getAngle')
        .then(res => {
          return res.json();
        })
        .then(data => {
          setTemp(data.angle);
        });
    }, 1000);
    
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      fetch('http://127.0.0.1:5000/getRpm')
        .then(res => {
          return res.json();
        })
        .then(data => {
          setRpm(data.engine_speed);
        });
      }, 1000);
    
      return () => clearInterval(timer);
  }, []);

  function Svetlo() {
    console.log(svetlo);
    setSvetlo(!svetlo);
    postData('http://127.0.0.1:5000/setLightStatus', {"lights": !svetlo})
  }

  function Rychlost(value) {
    console.log(value);
    setRychlost(value);
    postData('http://127.0.0.1:5000/setSpeed', {"speed": value})
  }

  return (
    <div className="demo">
      <div className='vlak'>
      <Progress
        className="budik1"
        progress={rpm}
        max={500}
        subtitle="RPM"
        reduction={0.25}
        hideBall
        strokeWidth={10}
        gradient={[{stop: 0.0, color: '#f6416d'}, {stop: 1, color: '#fa6d7c'}]} />
      <Progress
      className="budik2"
        progress={speed}
        max={100}
        subtitle="km/h"
        reduction={0.25}
        hideBall
        strokeWidth={10} />
      <Progress
      className="budik3"
        progress={temp}
        min={-45}
        max={45}
        subtitle="° (naklon)"
        strokeWidth={10}
        reduction={0.25}
        hideBall
        gradient={[{stop: 0.0, color: '#f6416d'}, {stop: 1, color: '#fa6d7c'}]} />  
        </div>
        <input id='svetla' class="svetla" onClick={Svetlo} checked={svetlo} type='checkbox'></input>
        <label class="button a" htmlFor='svetla'>Světla</label>
        <button class="button b">Katapult</button>
        <button class="button c">Klakson</button>
        <button class="button d">Z. Brzda</button>
        <div style={parentStyle}>
          <div style={style} className="rychlost">
            <Slider vertical min={-50} max={50} step={2} marks={marks} included={false} onAfterChange={Rychlost} defaultValue={0}/>
          </div>
        </div>
        </div>
  )
}

ReactDOM.render(<App />, document.getElementById('root'))