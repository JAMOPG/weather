import useSWR from "swr";
import fetcher from "../lib/fetcher";

const apiUrl = "http://localhost:8000/api/historics";

export function useHistoric(endpoint, dated) {
  const { data, error } = useSWR(
    `${apiUrl}/${endpoint}/?date=${dated}`,
    fetcher
  );

  if (endpoint === "search_date") {
    return {
      search_date: data?.user ? mapResponseProperties(data) : null,
      isLoading: !data && !error,
      isError: error,
    };
  }
}
function mapResponseProperties(data) {
  const mapped = {
    user: data.user,
    city: data.city,
    date: data.date,
  };

  // remove undefined fields
  Object.entries(mapped).map(
    ([key, value]) => value === undefined && delete mapped[key]
  );
  console.log(mapped);
  return mapped;
}
