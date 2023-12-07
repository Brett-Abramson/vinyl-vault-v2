import { ChangeEvent } from "react";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";

interface Props {
  label: string;
  name: string;
  type: string;
  handleChange: (event: ChangeEvent<HTMLInputElement>) => void;
  value: string;
  children: React.ReactNode;
  required?: boolean;
  fullWidth?: boolean;
}

const Input = ({
  label,
  name,
  type,
  handleChange,
  value,
  children,
  required = false,
}: Props) => {
  return (
    <Grid item xs={12} sm={6}>
      <TextField
        id={name}
        name={name}
        fullWidth
        label={label}
        type={type}
        onChange={handleChange}
        value={value}
        required={required}
      />
    </Grid>
  );
};

export default Input;

{
  /* <Input>First Name</Input> */
}
