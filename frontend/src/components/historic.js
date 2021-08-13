import React from "react";
import { useHistoric } from "../hooks/useHistoric";
import Loading from "./loading";

const Historic = ({ dated }) => {
  const { search_date, isLoading, isError } = useHistoric("search_date", dated);
  

  if (isLoading || isError) return <Loading />;
  return (
    <table className="table table-striped ">
      <thead class="thead-light">
        <tr>
          <th scope="col">User</th>
          <th scope="col">City</th>
          <th scope="col">Date</th>
        </tr>
      </thead>
      <tbody>
      {search_date.map(function(d, idx){
         return (<tr><td>{d.user}</td>
                <td>{d.city}</td>
                <td>{d.date}</td>
                </tr>)
       })}
       
      </tbody>
    </table>
  );
};

export default Historic;
