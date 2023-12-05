import { useSelector, useDispatch, TypedUseSelectorHook } from "react-redux";
import type { RootState, AppDispatch } from "./store";

// useAppDispatch esures that any actions dispatched using this hook are type-checked against the types defined in my store's dispatch function. This enhances type-safety and helps catch errors

// useAppSelector selects a part of the Redux state. any state selected using this hook is checked against the structure of my root Redux state

export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
