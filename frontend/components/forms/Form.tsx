import { FormEvent } from "react";
import Box from "@mui/material/Box";

interface Props {
  handleSubmit: (event: FormEvent<HTMLFormElement>) => void;
}

const Form = ({ handleSubmit }: Props) => {
  return (
    <Box
      component="form"
      noValidate
      onSubmit={handleSubmit}
      sx={{ mt: 3 }}
    ></Box>
  );
};

export default Form;
