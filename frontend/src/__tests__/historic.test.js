import React from "react";
import { render, screen } from "../app-test-utils";
import Historic from "../components/historic";

const renderHistoric = () => render(<Historic />);

describe("<Historic />", () => {
  test("renders the historic page", async () => {
    renderHistoric();
    expect(
      screen.getByRole("heading", { name: /historic reactweather/i })
    ).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: /openweathermap api/i })
    ).toBeInTheDocument();
    expect(screen.getByRole("link", { name: /react/i })).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: /tailwindcss/i })
    ).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: /erik flowers' weather icons/i })
    ).toBeInTheDocument();
  });
});
