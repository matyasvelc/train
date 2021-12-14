import React from 'react'
import ReactDOM from 'react-dom'
import Progress from './lib/progress'
import './styles.css'

function speed() {
  return fetch('http://127.0.0.1:5000/getSpeed')
  .then(response => response.json())
  .then(responseJson => {
    return responseJson.speed;
  })
  .catch((error) => {
    console.error(error);
  });
}

function App() {
  const [p1] = React.useState(20)
  const [p2] = React.useState(20)
  const [p3] = React.useState(2)

  return (
    <div className="demo">
      <Progress
        progress={p3}
        max={4}
        subtitle="*1000 rpm"
        reduction={0.25}
        hideBall
        strokeWidth={10}
        gradient={[{stop: 0.0, color: '#f6416d'}, {stop: 1, color: '#fa6d7c'}]} />
      <Progress
        progress={p1}
        max={100}
        subtitle="km/h"
        reduction={0.25}
        hideBall
        strokeWidth={10} />
      <Progress
        progress={p2}
        max={50}
        subtitle="°C"
        strokeWidth={10}
        reduction={0.25}
        hideBall
        gradient={[{stop: 0.0, color: '#f6416d'}, {stop: 1, color: '#fa6d7c'}]} />
    </div>
  )
}

ReactDOM.render(<App />, document.getElementById('root'))