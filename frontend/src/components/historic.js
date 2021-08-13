import React from "react";
import { useHistoric } from "../hooks/useHistoric";
import Loading from "./loading";

const Historic = ({ dated }) => {
  const { search_date, isLoading, isError } = useHistoric("search_date", dated);

  if (isLoading || isError) return <Loading />;
  debugger;
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
        <tr>
          <td>{search_date.user}</td>
          <td>{search_date.user}</td>
          <td>{search_date.user}</td>
        </tr>
        <tr>
          <td>{search_date.user}</td>
          <td>{search_date.user}</td>
          <td>{search_date.user}</td>
        </tr>
      </tbody>
    </table>
  );
};

export default Historic;
