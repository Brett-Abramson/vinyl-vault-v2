import { ChangeEvent } from "react";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";

interface Props {
  labelId: string;
  type: string;
  handleChange: (event: ChangeEvent<HTMLInputElement>) => void;
  value: string;
  children: React.ReactNode;
  required?: boolean;
  fullWidth?: boolean;
}

const Input = ({
  labelId,
  type,
  handleChange,
  value,
  children,
  required = false,
  fullWidth = false,
}: Props) => {
  return (
    <Grid item xs={12} sm={6}>
      <TextField
        name={labelId}
        fullWidth={fullWidth}
        id={labelId}
        label={labelId}
        onChange={handleChange}
        value={value}
        required={required}
        autoFocus
      />
    </Grid>
  );
};

export default Input;

{
  /* <Input>First Name</Input> */
}
