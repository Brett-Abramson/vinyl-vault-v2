import NextLink from "next/link";
import MuiLink from "@mui/material/Link";
import { TypographyProps } from "@mui/material/Typography";
import { ReactNode } from "react";

interface Props {
  href: string;
  underline?: "none" | "hover" | "always";
  variant?: TypographyProps["variant"];
  children: ReactNode;
}

const CustomLink = ({
  href,
  underline = "hover",
  variant = "body2",
  children,
}: Props) => {
  return (
    <MuiLink
      component={NextLink}
      href={href}
      underline={underline}
      variant={variant}
    >
      {children}
    </MuiLink>
  );
};

export default CustomLink;