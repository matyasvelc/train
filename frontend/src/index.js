import React, { useEffect } from 'react'
import ReactDOM from 'react-dom'
import Progress from './lib/progress'
import './styles.css'
import Slider, { Range } from 'rc-slider';
import 'rc-slider/assets/index.css';

function App() {
  const [temp, setTemp] = React.useState()
  const [rpm, setRpm] = React.useState()
  const [speed, setSpeed] = React.useState()

  useEffect(() => {
    const timer = setTimeout(() => {
      fetch('http://127.0.0.1:5000/getSpeed')
        .then(res => {
          return res.json();
        })
        .then(data => {
          setSpeed(data.Speed);
        });
    }, 1000);
    
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/getAngle')
      .then(res => {
        return res.json();
      })
      .then(data => {
        setTemp(data.Temperature);
      });
  }, []);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/getRpm')
      .then(res => {
        return res.json();
      })
      .then(data => {
        setRpm(data.RPM);
      });
  }, []);


  return (
    <div className="demo">
      <Progress
        progress={rpm}
        max={4}
        subtitle="*1000 rpm"
        reduction={0.25}
        hideBall
        strokeWidth={10}
        gradient={[{stop: 0.0, color: '#f6416d'}, {stop: 1, color: '#fa6d7c'}]} />
      <Progress
        progress={speed}
        max={100}
        subtitle="km/h"
        reduction={0.25}
        hideBall
        strokeWidth={10} />
      <Progress
        progress={temp}
        min={-45}
        max={45}
        subtitle="° (naklon)"
        strokeWidth={10}
        reduction={0.25}
        hideBall
        gradient={[{stop: 0.0, color: '#f6416d'}, {stop: 1, color: '#fa6d7c'}]} />
        <input id='svetla' class="svetla" type='checkbox'></input>
        <label class="button" htmlFor='svetla'>Světla</label>
        <button class="button" >Katapult</button>
        <button class="button" >Klakson</button>
        <button class="button" >Z. Brzda</button>
        <Slider min={-50} max={50} defaultValue={0} vertical={true}/>
    </div>
  )
}

ReactDOM.render(<App />, document.getElementById('root'))