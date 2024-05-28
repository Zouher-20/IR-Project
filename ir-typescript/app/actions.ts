"use server";

const urlWithDataset = (ds: string) => `${process.env.IR_BASE_URL}/${ds}`;

export const search = async (
  query: string,
  dataset: string
): Promise<Array<any>> => {
  return new Promise(async (resolve, reject) => {
    let url = urlWithDataset(dataset);
    await fetch(url + "?" + new URLSearchParams({ query }), {
      method: "GET",
    })
      .then((res) => res.json())
      .then((res) => {
        resolve(res);
      })
      .catch(() => reject());
  });
};
