import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Workouts = () => {
  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Workouts</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Workout</th>
              <th>Duration</th>
              <th>Calories</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Yoga</td>
              <td>60 mins</td>
              <td>200</td>
            </tr>
            <tr>
              <td>Weightlifting</td>
              <td>45 mins</td>
              <td>350</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Workouts;
