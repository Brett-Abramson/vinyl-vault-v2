import { useEffect } from "react";
import { useAppDispatch } from "@/redux/hooks";
import { setAuth, finishIntialLoad } from "@/redux/features/authSlice";
import { useVerifyMutation } from "@/redux/features/authApiSlice";

const useVerify = () => {
  const dispatch = useAppDispatch();

  const [verify] = useVerifyMutation();

  useEffect(() => {
    verify(undefined)
      .unwrap()
      .then(() => {
        dispatch(setAuth());
      })
      .finally(() => {
        dispatch(finishIntialLoad());
      });
  }, []);
};

export default useVerify;
