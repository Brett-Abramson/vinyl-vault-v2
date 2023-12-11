import NextLink from "next/link";
import MuiLink from "@mui/material/Link";
import { TypographyProps } from "@mui/material/Typography";
import { ReactNode } from "react";
import { Button } from "@mui/material";


interface Props {
  href?: string;
  underline?: "none" | "hover" | "always";
  variant?: TypographyProps["variant"];
  color?: TypographyProps["color"];
  children?: ReactNode;
  [rest: string]: any;
}

const CustomLink = ({
  href,
  underline = "hover",
  variant = "inherit",
  color = "inherit",
  children,
  ...rest
}: Props) => {

  if (!href) {
    return ( 
    <Button onClick={rest.onClick}>{children}</Button>
    )
  }
  return (
    <MuiLink
      component={NextLink}
      href={href}
      underline={underline}
      variant={variant}
      color={color}
    >
      {children}
    </MuiLink>
  );
};

export default CustomLink;
