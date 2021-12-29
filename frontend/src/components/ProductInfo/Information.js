import React, { useState } from "react";
import GlobalModal from "../GlobalModal/GlobalModal";
import "../GlobalModal/GlobalModal.css";

const Information = ({ productInfo }) => {
  const [updatedValue, setUpdatedValue] = useState({});

  const [isOpen, setIsOpen] = useState(false);
  const togglePopup = () => {
    setIsOpen(!isOpen);
  };

  const handleChange = (event) => {
    setUpdatedValue({ [event.target.name]: event.target.value });
    console.log("updatedValue", updatedValue);
  };

  return (
    <div>
      <h1>Products</h1>
      <table
        id="dtBasicExample"
        class="table table-striped table-bordered table-sm"
        cellspacing="0"
        width="100%"
      >
        <thead>
          <tr>
            <th className="table__item_header">#</th>
            <th className="table__item_header">Title</th>
            <th className="table__item_header">Description</th>
            <th className="table__item_header">Variant</th>
            <th className="table__item_header">Price</th>
            <th className="table__item_header">Stock</th>
            <th className="table__item_header">Action</th>
          </tr>
        </thead>
        <tbody>
          {productInfo.products.map((product, productIndex) => {
            var hourStart = new Date(`${product.created_at}`);
            var hourEnd = new Date();

            var hourDiff = hourEnd - hourStart;

            hourDiff = Math.round(hourDiff / 60 / 60 / 1000);

            const day = Math.round(hourDiff / 24);
            const hour = hourDiff % 24;

            return (
              <tr role="row" className="table__row">
                <td className="table__item">{product.id}</td>
                <td className="table__item">
                  {product.title}
                  <br />
                  Created at {day && `${day} days`} and{" "}
                  {hour && `${hour} hours`} ago
                </td>
                <td className="table__item_desc">{product.description}</td>
                <td className="table__item">
                  {productInfo.variants.map((variant, variantIndex) => {
                    return (
                      <>
                        {productInfo.productVariants.map(
                          (productVariant, productVariantIndex) => {
                            if (
                              productVariant.variant_id === variant.id &&
                              productVariant.product_id === product.id
                            ) {
                              return (
                                <>
                                  <span className="custom_wr">
                                    {productVariant.variant_title}/
                                    {variant.title}
                                    <br />
                                  </span>
                                </>
                              );
                            }
                          }
                        )}
                      </>
                    );
                  })}
                </td>
                <td className="table__item">
                  {productInfo.variants.map((variant, variantIndex) => {
                    return (
                      <>
                        {productInfo.productVariants.map(
                          (productVariant, productVariantIndex) => {
                            if (
                              productVariant.variant_id === variant.id &&
                              productVariant.product_id === product.id
                            ) {
                              return (
                                <>
                                  <span className="custom_wr">
                                    {productVariant.price}
                                    <br />
                                  </span>
                                </>
                              );
                            }
                          }
                        )}
                      </>
                    );
                  })}
                </td>
                <td className="table__item">
                  {productInfo.variants.map((variant, variantIndex) => {
                    return (
                      <>
                        {productInfo.productVariants.map(
                          (productVariant, productVariantIndex) => {
                            if (
                              productVariant.variant_id === variant.id &&
                              productVariant.product_id === product.id
                            ) {
                              return (
                                <>
                                  <span className="custom_wr">
                                    {productVariant.stock}
                                    <br />
                                  </span>
                                </>
                              );
                            }
                          }
                        )}
                      </>
                    );
                  })}
                </td>
                <td className="table__item">
                  <button onClick={togglePopup}>Edit</button>
                  <GlobalModal
                    open={isOpen}
                    onClose={togglePopup}
                    className={"form__builder__modal ar__options_modal"}
                  >
                    <div>
                      <form method="POST" action="">
                        <label for="title">Title</label>
                        <br />
                        <input
                          type="text"
                          id="title"
                          name="title"
                          defaultValue="Title"
                          onChange={handleChange}
                        />
                        <br />
                        <br />
                        <label for="description">Description</label>
                        <br />
                        <textarea
                          className="description__edit"
                          id="description"
                          name="description"
                          rows="4"
                          cols="50"
                          defaultValue="Description"
                          onChange={handleChange}
                        ></textarea>
                        <br />
                        <br />

                        <label for="variants">Choose a color:</label>
                        <select name="colors" id="colors">
                          <option defaultValue="Red" onChange={handleChange}>
                            Red
                          </option>
                        </select>
                        <br />
                        <br />

                        <label for="variants">Choose a size:</label>
                        <select name="variants" id="variants">
                          <option defaultValue="XXL" onChange={handleChange}>
                            XXL
                          </option>
                        </select>
                        <br />
                        <br />

                        <label for="price">Price</label>
                        <br />
                        <input
                          type="number"
                          id="price"
                          name="price"
                          defaultValue="10"
                          onChange={handleChange}
                        />
                        <br />
                        <br />

                        <label for="stock">Stock</label>
                        <br />
                        <input
                          type="number"
                          id="stock"
                          name="stock"
                          defaultValue="20"
                          onChange={handleChange}
                        />

                        <br />
                        <br />
                        <input type="submit" value="Submit" />
                      </form>
                    </div>
                  </GlobalModal>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default Information;
